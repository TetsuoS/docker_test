FROM python:3.6
ARG work_dir=/work/
ADD pure_flask $work_dir/pure_flask

WORKDIR $work_dir

RUN pip install -r pure_flask/requirements.txt
CMD python pure_flask/app.run