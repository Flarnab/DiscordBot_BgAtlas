import requests
import collections

GameResult = collections.namedtuple(
    'GameResult',
    'id,name,year_published,min_players,max_players,min_playtime,max_playtime,min_age,description,'
    'description_preview,image_url,thumb_url,images,url,msrp,price,discount,primary_publisher,publishers,mechanics,'
    'categories,designers,developers,artists,names,num_user_ratings,average_user_rating,official_url,rules_url,'
    'weight_amount,weight_units,size_height,size_width,size_depth,size_units,matches_specs,spec,'
    'reddit_all_time_count,reddit_week_count,reddit_day_count,historical_low_price,historical_low_date '
)

search = input("What game are you looking for?")
url = 'https://www.boardgameatlas.com/api/search?name={}&client_id=i9OKci4zRl'.format(search)

resp = requests.get(url)
resp.raise_for_status()

game_data = resp.json()
games_list = game_data.get('games')
print(game_data)

games = []
for gd in games_list:
    g = GameResult(
        id=gd.get('id'),
        name=gd.get('name'),
        year_published=gd.get('year_published'),
        min_players=gd.get('min_players'),
        max_players=gd.get('max_players'),
        min_playtime=gd.get('min_playtime'),
        max_playtime=gd.get('max_playtime'),
        min_age=gd.get('min_age'),
        description=gd.get('description'),
        description_preview=gd.get('description_preview'),
        image_url=gd.get('image_url'),
        thumb_url=gd.get('thumb_url'),
        images=gd.get('images'),
        url=gd.get('url'),
        msrp=gd.get('msrp'),
        price=gd.get('price'),
        discount=gd.get('discount'),
        primary_publisher=gd.get('primary_publisher'),
        publishers=gd.get('publishers'),
        mechanics=gd.get('mechanics'),
        categories=gd.get('categories'),
        designers=gd.get('designers'),
        developers=gd.get('developers'),
        artists=gd.get('artists'),
        names=gd.get('names'),
        num_user_ratings=gd.get('num_user_ratings'),
        average_user_rating=gd.get('average_user_rating'),
        official_url=gd.get('official_url'),
        rules_url=gd.get('rules_url'),
        weight_amount=gd.get('weight_amount'),
        weight_units=gd.get('weight_units'),
        size_height=gd.get('size_height'),
        size_width=gd.get('size_width'),
        size_depth=gd.get('size_depth'),
        size_units=gd.get('size_units'),
        matches_specs=gd.get('matches_specs'),
        spec=gd.get('spec'),
        reddit_all_time_count=gd.get('reddit_all_time_count'),
        reddit_week_count=gd.get('reddit_week_count'),
        reddit_day_count=gd.get('reddit_day_count'),
        historical_low_price=gd.get('historical_low_price'),
        historical_low_date=gd.get('historical_low_date')
    )
    games.append(g)

games = [
    GameResult(**gd)
    for gd in games_list
]

print("Found {} games for search {}".format(len(games), search))
for g in games:
    print("{} -- {}".format(g.year_published, g.name))
