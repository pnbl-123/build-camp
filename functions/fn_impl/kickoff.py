from firebase_functions import https_fn
import sys
from fn_impl.crew import (
    CrewaiEnterpriseContentMarketingCrew,
)

@https_fn.on_request()
def kickoff(req: https_fn.Request) -> https_fn.Response:
    """
    Run the crew.
    """
    inputs = {"topic": "AI Agent Framework", "company": "CrewAI"}
    output = CrewaiEnterpriseContentMarketingCrew().crew().kickoff(inputs=inputs)
    return https_fn.Response(output.raw, mimetype="text/plain")  # Plain text response

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI Agent Framework", "company": "CrewAI"}
    try:
        CrewaiEnterpriseContentMarketingCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiEnterpriseContentMarketingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI Agent Framework", "company": "CrewAI"}
    try:
        CrewaiEnterpriseContentMarketingCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
