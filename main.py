# importing uvicorn library
# it is a lightning-fast ASGI server implementation, using uvloop and httptools
# ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to
# provide a standard interface between async-capable Python web servers, frameworks, and applications
import uvicorn
# importing fastapi framework
# a web framework for building apis with python
from fastapi import FastAPI
# importing RedirectResponse from fastapi responses package
# returns an http redirect
from fastapi.responses import RedirectResponse

# import evaluate function from evaluate module in controllers package
from controllers.main_controller import evaluate
# import Answer model class from Answer module in models package
from models.Answer import Answer
# import Results model class from Result module in models package
from models.Result import Result

# creating an application instance
app = FastAPI(title='Semantic Similarity API',
              description='Semantic Similarity API',
              version='1.0.0',
              openapi_url='/semantic-similarity-api.json',
              docs_url='/docs',
              redoc_url='/redoc',
              swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect',
              swagger_ui_init_oauth=None,
              openapi_prefix='',
              root_path='',
              root_path_in_servers=True,
              include_in_schema=True)


# redirecting to swagger docs
@app.get('/',
         tags=['redirect-to-swagger'],
         response_model=None,
         status_code=200,
         summary='Redirect to Swagger Docs',
         description='Redirect the fastapi application to swagger documentation.',
         response_description='Successful Response')
async def root():
    return RedirectResponse(url='/docs')


# http post api getting answer class object as inputs and returns the evaluate function
@app.post('/semantic-similarity/',
          tags=['semantic-similarity'],
          response_model=Result,
          status_code=200,
          summary='Student Answer Evaluation',
          description='Evaluating student answers and returning scores for each criterion.',
          response_description='Successful Response')
async def evaluate_answer(answers: Answer):
    return evaluate(answers)


# running the application on a local development server
if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=8000)
