"""Some Feature feature tests."""
from .conftest import log,get_dataframe
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)
@scenario('../features/demo.feature', 'Fare check')
def test_s1():
    log.info("in test_s1")


@given(parsers.cfparse('Get "{stream}" dataset from "{file}"'))
def given_step(context,stream,file):
    log.info(f"Given Step Started for Stream : {stream} and Dataset : {file}.")
    df = get_dataframe(stream,file)
    context[stream] = df
    log.info('Given Step Finished.')


@when(parsers.cfparse('Filter "{col}" column from "{stream}"'))
def when_step(context,col,stream):
    log.info(f"When Step Started for Column : {col} and Stream : {stream}")
    df = context[stream]
    df_col = df[col]
    context[f"{col}_{stream}"] = df_col
    log.info('When Step Finished.')


@then(parsers.cfparse('Verify "{col1}" + "{per:d}" pecentage for "{stream1}" == "{col2}" for "{stream2}" == "{col3}" for "{stream3}"'))
def then_step(context,col1,col2,col3,per,stream1,stream2,stream3):
    log.info(f"Then Step Started.")
    df_col1 = context[f"{col1}_{stream1}"]
    df_col2 = context[f"{col2}_{stream2}"]
    df_col3 = context[f"{col3}_{stream3}"]
    df_col1 = df_col1 + (df_col1*per)/100
    #assert df_col1.equals(df_col2)
    #assert df_col2.equals(df_col3)
    log.info('Then Step Finished.')
    

