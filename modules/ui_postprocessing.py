import gradio as gr
from modules import scripts_postprocessing, scripts, shared, gfpgan_model, codeformer_model, ui_common, postprocessing, \
    call_queue
import modules.generation_parameters_copypaste as parameters_copypaste


def create_ui():
    tab_index = gr.State(value=0)

    with gr.Row().style(equal_height=False, variant='compact'):
        with gr.Column(variant='compact'):
            with gr.Tabs(elem_id="mode_extras"):
                with gr.TabItem('单个处理', elem_id="extras_single_tab") as tab_single:
                    extras_image = gr.Image(label="上传图片", source="upload", interactive=True, type="pil",
                                            elem_id="extras_image")

                with gr.TabItem('批量处理', elem_id="extras_batch_process_tab") as tab_batch:
                    image_batch = gr.File(label="批量处理", file_count="multiple", interactive=True, type="file",
                                          elem_id="extras_image_batch")

                with gr.TabItem('批量处理目录下的文件', elem_id="extras_batch_directory_tab") as tab_batch_dir:
                    extras_batch_input_dir = gr.Textbox(label="输入目录", **shared.hide_dirs,
                                                        placeholder="在此粘贴输入目录的地址",
                                                        elem_id="extras_batch_input_dir")
                    extras_batch_output_dir = gr.Textbox(label="输出目录", **shared.hide_dirs,
                                                         placeholder="在此粘贴输出目录的地址",
                                                         elem_id="extras_batch_output_dir")
                    show_extras_results = gr.Checkbox(label='显示结果图像', value=True,
                                                      elem_id="extras_show_extras_results")

            submit = gr.Button('开始生成', elem_id="extras_generate", variant='primary')

            script_inputs = scripts.scripts_postproc.setup_ui()

        with gr.Column():
            result_images, html_info_x, html_info, html_log = ui_common.create_output_panel("extras",
                                                                                            shared.opts.outdir_extras_samples)

    tab_single.select(fn=lambda: 0, inputs=[], outputs=[tab_index])
    tab_batch.select(fn=lambda: 1, inputs=[], outputs=[tab_index])
    tab_batch_dir.select(fn=lambda: 2, inputs=[], outputs=[tab_index])

    submit.click(
        fn=call_queue.wrap_gradio_gpu_call(postprocessing.run_postprocessing, extra_outputs=[None, '']),
        inputs=[
            tab_index,
            extras_image,
            image_batch,
            extras_batch_input_dir,
            extras_batch_output_dir,
            show_extras_results,
            *script_inputs
        ],
        outputs=[
            result_images,
            html_info_x,
            html_info,
        ]
    )

    parameters_copypaste.add_paste_fields("extras", extras_image, None)

    extras_image.change(
        fn=scripts.scripts_postproc.image_changed,
        inputs=[], outputs=[]
    )
