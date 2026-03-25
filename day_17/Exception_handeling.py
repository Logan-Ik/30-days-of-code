# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# nordic_countries = ['Finland', 'Sweden', 'Norway','Denmark', 'Iceland']
# es = 'Estonia'
# ru = 'Russia'
# nordic_countries.append(es)
# nordic_countries.append(ru)
# print(nordic_countries)  

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names

print("Nordic Countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)