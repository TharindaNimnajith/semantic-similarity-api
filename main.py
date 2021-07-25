import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from controllers.main_controller import evaluate
from models.Answer import Answer
from models.Result import Result

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

origins = [
    'https://localhost:5001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/',
         tags=['redirect-to-swagger'],
         response_model=None,
         status_code=200,
         summary='Redirect to Swagger Docs',
         description='Redirect the fastapi application to swagger documentation.',
         response_description='Successful Response')
async def root():
    return RedirectResponse(url='/docs')


@app.post('/semantic-similarity/',
          tags=['semantic-similarity'],
          response_model=Result,
          status_code=200,
          summary='Student Answer Evaluation',
          description='Evaluating student answers and returning scores for each criterion.',
          response_description='Successful Response')
async def evaluate_answer(answers: Answer):
    return evaluate(answers)


if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=8000)
