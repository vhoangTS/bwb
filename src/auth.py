import pandas as pd
import os


def create_dummy_user_database():
    """
    Dummy database for authentication & authorization example.
    """
    """
    username    password    access-type
    admin       foo         full
    vhoang      bar         limited
    """

    dummy_data = {
        'username': ['admin', 'vhoang'],
        'password': ['foo', 'bar'],
        'access-type': ['full', 'limited']
    }
    pd.DataFrame(data=dummy_data).to_pickle('database.pickle')


def load_dummy_user_database(file='database.pickle'):
    """
    Convert user database binary file to pandas dataframe.

    :param file: Database file name. Default dummy database.pickle.
    :return: Dataframe consists of username, password and role.
    """
    if os.path.isfile(file):
        return pd.read_pickle(file)
    else:
        raise OSError('User-database not found!')


def add_user_to_dummy_database(user, pswd, role, file='database.pickle'):
    """
    A function to append a new user to existing database.
    TODO: Currently it appends directly at the end without checking, which can result user entry duplication.

    :param user: Username.
    :param pswd: Password.
    :param role: Role.
    :param file: Database filename. Default dummy database.pickle.
    """
    df_base = load_dummy_user_database(file)
    df_add = pd.DataFrame(data={'username': [user],
                                'password': [pswd],
                                'access-type': [role]})
    df = pd.concat([df_base, df_add])
    df.to_pickle(file)


def check_login_data(user, pswd, df):
    """
    Check if an user&pswd pair exist in database or not.

    :param user: Username.
    :param pswd: Pasword.
    :param df: User database as pandas dataframe.
    :return: True if user exist.
    """
    return ((df['username'] == user) & (df['password'] == pswd)).any()


def get_user_role(user, pswd, df):
    """
    Get role of specific user&pswd pair.

    :param user:  Username.
    :param pswd: Password.
    :param df: User database as pandas dataframe.
    :return: Return access type of first user&pswd pair found, 'no-access' if user not found.
    """
    if check_login_data(user, pswd, df):
        return df.loc[(df['username'] == user) & (df['password'] == pswd)].iloc[0]['access-type']
    else:
        return 'no-access'


if __name__ == '__main__':
    # create_dummy_user_database()
    data = load_dummy_user_database()
    print(data)
    print(get_user_role(user='admin', pswd='foo', df=data))
