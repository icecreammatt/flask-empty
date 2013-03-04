from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.repository import *

mod = Blueprint('core', __name__)

@mod.route('/')
def index():
  repository = Repository()
  return (render_template('core/index.html', resources=repository.getResources()))
