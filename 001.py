import random

# 餐厅列表和对应的菜品列表
restaurants = {
    '汉堡王': ['双层牛肉芝士堡', '原味鸡块', '薯条', '可乐'],
    '必胜客': ['海鲜比萨', '鸡肉沙拉', '薯条', '可乐'],
    '麦当劳': ['麦香鸡', '双层牛肉汉堡', '薯条', '可乐'],
    '肯德基': ['香辣鸡翅', '新奥尔良烤鸡腿', '薯条', '可乐'],
    '星巴克': ['拿铁咖啡', '抹茶星冰乐', '烤肠', '蓝莓饼干'],
    '鲜芋仙': ['芋圆奶茶', '黑糯米鲜奶', '红豆抹茶奶盖'],
    '盒马鲜生': ['水饺', '蒸包', '糯米鸡', '海鲜盖浇饭']
}

# 用户的偏好
preferences = {
    'meat': True,  # 是否吃肉
    'vegetable': False,  # 是否吃蔬菜
    'spicy': True,  # 是否喜欢辣
    'sweet': True  # 是否喜欢甜
}

# 筛选符合用户偏好的餐厅和菜品
candidate_restaurants = []
for restaurant, dishes in restaurants.items():
    candidate_dishes = []
    for dish in dishes:
        if preferences['meat'] and ('牛肉' in dish or '鸡肉' in dish or '猪肉' in dish):
            candidate_dishes.append(dish)
        elif preferences['vegetable'] and ('蔬菜' in dish or '沙拉' in dish):
            candidate_dishes.append(dish)
        elif preferences['spicy'] and '辣' in dish:
            candidate_dishes.append(dish)
        elif preferences['sweet'] and '甜' in dish:
            candidate_dishes.append(dish)
    if candidate_dishes:
        candidate_restaurants.append((restaurant, candidate_dishes))

# 随机选择一个餐厅和一道菜品
if candidate_restaurants:
    restaurant, dishes = random.choice(candidate_restaurants)
    dish = random.choice(dishes)
    print(f'今天去{restaurant}吃{dish}吧！')
else:
    print('很抱歉，没有符合你偏好的餐厅和菜品。')
