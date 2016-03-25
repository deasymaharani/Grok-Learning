def is_capital(state,city):
    dic_state = {'New South Wales': 'Sydney',
                 'Queensland':'Brisbane',
                 'South Australia': 'Adelaide',
                 'Tasmania': 'Hobart',
                 'Victoria':'Melbourne',
                 'Western Australia':'Perth'}
    if state not in dic_state.keys() or city not in dic_state.values():
        return False
    else:
        if city == dic_state[state]:
            return True
        else:
            return False