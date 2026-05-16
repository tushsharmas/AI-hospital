import gradio as gr

from graph.workflow import graph


def run_agent(user_input):

    result = graph.invoke({
        "user_input": user_input
    })

    routing = result.get("routing_decision")

    specialist = result.get("specialist_response")

    if routing:

        specialist_name = routing.specialty

        assessment = routing.initial_assessment

        reason = routing.reason

    else:

        specialist_name = "None"

        assessment = "No assessment"

        reason = "No reason"


    if specialist:

    final_message = specialist["messages"][-1].content

    condition = final_message

    severity = "Analyzed by specialist agent"

    recommendations = "See specialist response above"

    else:

        condition = "No specialist needed"

        severity = "-"

        recommendations = "-"


    return (
        specialist_name,
        assessment,
        reason,
        condition,
        severity,
        recommendations
    )


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 🏥 Multi-Agent AI Hospital System
        
        Enter symptoms and the AI orchestrator
        will route the patient to the correct specialist.
        """
    )

    with gr.Row():

        user_input = gr.Textbox(
            label="Patient Symptoms",
            placeholder="Example: chest pain, breathing difficulty..."
        )

    analyze_btn = gr.Button(
        "Analyze Patient"
    )

    gr.Markdown("## 🧠 Orchestrator Decision")

    with gr.Row():

        specialist_output = gr.Textbox(
            label="Selected Specialist"
        )

        assessment_output = gr.Textbox(
            label="Initial Assessment"
        )

    reason_output = gr.Textbox(
        label="Routing Reason"
    )

    gr.Markdown("## 👨‍⚕️ Specialist Diagnosis")

    with gr.Row():

        condition_output = gr.Textbox(
            label="Condition"
        )

        severity_output = gr.Textbox(
            label="Severity"
        )

    recommendation_output = gr.Textbox(
        label="Recommendations",
        lines=6
    )

    analyze_btn.click(
        fn=run_agent,
        inputs=user_input,
        outputs=[
            specialist_output,
            assessment_output,
            reason_output,
            condition_output,
            severity_output,
            recommendation_output
        ]
    )

demo.launch()