FROM python:3.6
ARG work_dir=/work/

WORKDIR $work_dir/resource

ADD resource $work_dir/resource
ADD resource $work_dir/resource
RUN pip install -r requirements.txt
CMD ["python", "/work/resource/app.py"]