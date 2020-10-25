from flask import Flask, render_template, request, redirect, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
import urllib.request
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '3358a36bc2b3179feb0372717386ad2dfdee92c60f2de818c5ef7562a44d8c0a25bac26d7043eaf3110e37c0683e999672362ec5fd4e8cf74fcd9f01100cbcc7c61c02f0d9aaa1984c85828f4e7ac2c4fc22c7989ec49d7c289f4377022071d41e7e7d77d1e1a51d4c7b224b71cb682c91ff7d466c0869b9d077ed512c591b7f1c2677bc0a3674f2dece66fddf9314d6ef34bdfbe19a6244bb1169'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)