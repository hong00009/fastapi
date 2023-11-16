# coding: utf-8
from sqlalchemy import (Column, String, Text, CHAR, DateTime, Boolean, ForeignKey)
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

# 새로 추가함
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True)  # 사용자 고유번호
    account = Column(String(255))  # 계정/ID
    password = Column(String(255))  # 비밀번호
    name = Column(String(255))  # 이름
    user_type = Column(CHAR(1))  # 회원유형 0일반회원/1기업회원
    createdAt = Column(DateTime)  # 가입일자
    location = Column(String(255))  # 근무지


class Post(Base):
    __tablename__ = "post"
    post_id = Column(INTEGER, primary_key=True)  # 게시물 고유번호
    author_id = Column(INTEGER, ForeignKey(User.id))  #  작성자id
    title = Column(String(255))  # 게시물 제목
    content = Column(Text)  # 게시물 내용
    createdAt = Column(DateTime)  # 게시물작성일
    career = Column(CHAR(1))  # 경력: 경력무관0,신입1,경력2
    edu = Column(CHAR(1))  # 최종학력: 학력무관0,고졸1,초대졸2,대졸3,석사4,박사5
    start_date = Column(DateTime)  # 채용접수 시작일
    end_date = Column(DateTime)  # 채용접수 마감일
    is_public = Column(Boolean)  # 게시물 공개/비공개 여부
    analyze_result = Column(Text)  # 분석결과(직무12가지 퍼센티지%)
    use_template = Column(Boolean)  # 직무 템플릿 사용/비사용(커스텀)


class Job(Base):
    __tablename__ = "job"
    job_id = Column(INTEGER, primary_key=True)  # 직무(job) 고유번호
    job_title = Column(String(255))  # 직무명
    job_description = Column(Text)  # 직무설명


class Task(Base):
    __tablename__ = "task"
    task_id = Column(CHAR(5), primary_key=True)  # 업무(task) 고유번호
    task_title = Column(String(255))  # 업무명
    task_description = Column(Text)  # 업무설명


class Skill(Base):
    __tablename__ = "skill"
    skill_id = Column(CHAR(5), primary_key=True)  # 스킬 고유번호
    skill_title = Column(String(255))  # 스킬명
    skill_description = Column(Text)  # 스킬설명


class Knowledge(Base):
    __tablename__ = "knowledge"
    knowledge_id = Column(CHAR(5), primary_key=True)  # 지식 고유번호
    knowledge_title = Column(String(255))  # 지식명
    knowledge_description = Column(Text)  # 지식설명


class TaskSkill(Base):
    __tablename__ = "task_skill"
    taskskill_id = Column(INTEGER, primary_key=True)
    task_id = Column(CHAR(5), ForeignKey(Task.task_id))
    skill_id = Column(CHAR(5), ForeignKey(Skill.skill_id))

    # Task와 Skill 테이블과의 관계를 정의
    task = relationship('Task', back_populates='skills')
    skill = relationship('Skill', back_populates='tasks')

# Task 모델에 TaskSkill과의 일대다 관계 정의
Task.skills = relationship('TaskSkill', back_populates='task')

# Skill 모델에 TaskSkill과의 일대다 관계 정의
Skill.tasks = relationship('TaskSkill', back_populates='skill')


class TaskKnowledge(Base):
    __tablename__ = "task_knowledge"
    taskknowledge_id = Column(INTEGER, primary_key=True)
    task_id = Column(CHAR(5), ForeignKey(Task.task_id))
    knowledge_id = Column(CHAR(5), ForeignKey(Knowledge.knowledge_id))
    # Task와 Knowledge 테이블과의 관계를 정의
    task = relationship('Task', back_populates='knowledges')
    knowledge = relationship('Knowledge', back_populates='tasks')

# Task 모델에 TaskKnowledge와의 일대다 관계 정의
Task.knowledges = relationship('TaskKnowledge', back_populates='task')

# Knowledge 모델에 TaskKnowledge와의 일대다 관계 정의
Knowledge.tasks = relationship('TaskKnowledge', back_populates='knowledge')


class JobTask(Base):
    __tablename__ = "job_task"
    jobtask_id = Column(INTEGER, primary_key=True)
    job_id = Column(INTEGER, ForeignKey(Job.job_id))
    task_id = Column(CHAR(5), ForeignKey(Task.task_id))

    # Job와 Task 테이블과의 관계를 정의
    job = relationship('Job', back_populates='tasks')
    task = relationship('Task', back_populates='jobs')

# Job 모델에 JobTask와의 일대다 관계 정의
Job.tasks = relationship('JobTask', back_populates='job')

# Task 모델에 JobTask와의 일대다 관계 정의
Task.jobs = relationship('JobTask', back_populates='task')


class PostTask(Base):
    __tablename__ = "post_task"
    posttask_id = Column(INTEGER, primary_key=True)
    post_id = Column(INTEGER, ForeignKey(Post.post_id))
    task_id = Column(CHAR(5), ForeignKey(Task.task_id))

    # Post와 Task 테이블과의 관계를 정의
    post = relationship('Post', back_populates='tasks')
    task = relationship('Task', back_populates='posts')

# Post 모델에 PostTask와의 일대다 관계 정의
Post.tasks = relationship('PostTask', back_populates='post')

# Task 모델에 PostTask와의 일대다 관계 정의
Task.posts = relationship('PostTask', back_populates='task')



class PostJob(Base):
    __tablename__ = "post_job"
    postjob_id = Column(INTEGER, primary_key=True)
    post_id = Column(INTEGER, ForeignKey(Post.post_id))
    job_id = Column(CHAR(5), ForeignKey(Job.job_id))

    # Post와 Jobs 테이블과의 관계를 정의
    post = relationship('Post', back_populates='jobs')
    job = relationship('Job', back_populates='posts')

# Post 모델에 PostJob과의 일대다 관계 정의
Post.jobs = relationship('PostJob', back_populates='post')

# Job 모델에 PostJob과의 일대다 관계 정의
Job.posts = relationship('PostJob', back_populates='job')