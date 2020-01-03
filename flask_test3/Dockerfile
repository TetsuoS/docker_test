FROM python:3.6
ARG work_dir=/work/
ADD pure_flask $work_dir/pure_flask

WORKDIR $work_dir/pure_flask

RUN pip install -r requirements.txt
CMD ["python", "/work/pure_flask/app.py"]