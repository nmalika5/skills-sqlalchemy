"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.]
Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(or_(Brand.founded < 1950, Brand.discontinued.isnot(None))).all()

Brand.query.filter(or_(Brand.founded < 1950, Brand.discontinued != None)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter_by(year=year).all()

    for model in models:
        print model.brand_name, model.name, model.brand.headquarters 

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # Creating 3 different ways to handle this function

    # Using DISTINCT in my query to handle duplication

    models = Model.query.distinct('brand_name, name').order_by('brand_name').all()
    brand_name_dict = {}

    for model in models:
        if model.brand_name not in brand_name_dict:
            brand_name_dict[model.brand_name] = [model.name]
        else:
            brand_name_dict[model.brand_name].append(model.name)

    for brand in brand_name_dict:
        print brand + " MODELS of this BRAND: "

        for model in brand_name_dict[brand]:
            print "\t" + model

''' Version 2 - Using SET to handle the duplication of model names

    models = Model.query.all()

    brand_name_dict = {}

    for model in models:
        if model.brand_name not in brand_name_dict:
            brand_name_dict[model.brand_name] = [model.name]
        else:
            brand_name_dict[model.brand_name].append(model.name)

    for brand in brand_name_dict:
        print brand + " MODELS of this BRAND: "

        for model in set(brand_name_dict[brand]):
            print "\t" + model
'''

''' Using second dictionary for each brand to handle duplication of model names

    models = Model.query.all()

    brand_name_dict = {}

    for model in models:
        if model.brand_name not in brand_name_dict:
            brand_name_dict[model.brand_name] = {}
            brand_name_dict[model.brand_name][model.name] = model.year
        else:
            brand_name_dict[model.brand_name][model.name] = model.year

    for brand in brand_name_dict:
        print brand + " MODELS of this BRAND: "

        for model in brand_name_dict[brand]:
            print "\t" + model
'''

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Returns brand names that match a string"""

    string = '%' + mystr + '%'

    matching_brand_names = Brand.query.filter(or_(Brand.name.like(string), Brand.name == string)).all()

    return matching_brand_name


def get_models_between(start_year, end_year):
    """Returns models with years that are within a range"""

    models = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return models

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# ANSWER:

# An object that matches that criteria is returned. It is an object of a 
# class BaseQuery in flask_sqlalchemy. The value of the query is the question/query itself
# as we don't request the result/output by including all(), one() or first() methods. 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# ANSWER:

# An association table is meant to associate two tables togethe. It's not a middle 
# table as it doesn't have its own data. It's used to manage Many-To-Many relationship 
# between two classes/tables
