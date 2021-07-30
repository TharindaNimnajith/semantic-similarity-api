import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.middleware import Middleware

from controllers import main_controller_paraphrasing
from controllers import main_controller_summarization
from models.Answer import Answer
from models.Result import Result

middleware = [
    Middleware(CORSMiddleware,
               allow_credentials=True,
               allow_origins=['*'],
               allow_methods=['*'],
               allow_headers=['*'])
]

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
              include_in_schema=True,
              middleware=middleware)


@app.get('/',
         tags=['redirect-to-swagger'],
         response_model=None,
         status_code=200,
         summary='Redirect to Swagger Docs',
         description='Redirect the fastapi application to swagger documentation.',
         response_description='Successful Response')
async def root():
    return RedirectResponse(url='/docs')


@app.post('/paraphrasing',
          tags=['semantic-similarity'],
          response_model=Result,
          status_code=200,
          summary='Student Answer Evaluation for Paraphrasing',
          description='Evaluating student answers for paraphrasing activities and returning scores for each'
                      ' criterion with a comprehensive feedback.',
          response_description='Successful Response')
async def evaluate_answer(answers: Answer):
    return main_controller_paraphrasing.evaluate(answers)


@app.post('/summarization',
          tags=['semantic-similarity'],
          response_model=Result,
          status_code=200,
          summary='Student Answer Evaluation for Summarization',
          description='Evaluating student answers for summarization activities and returning scores for each'
                      ' criterion with a comprehensive feedback.',
          response_description='Successful Response')
async def evaluate_answer(answers: Answer):
    return main_controller_summarization.evaluate(answers)


if __name__ == '__main__':
    uvicorn.run('main:app',
                host='127.0.0.1',
                port=8000,
                reload=True,
                access_log=False)
