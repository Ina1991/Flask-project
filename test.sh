from app import Movie  # 导入模型类
movie = Movie.query.first()  # 获取 Movie 模型的第一个记录（返回模型类实例）
movie.title  # 对返回的模型类实例调用属性即可获取记录的各字段数据
#'Leon'
movie.year
#'1994'
Movie.query.all()  # 获取 Movie 模型的所有记录，返回包含多个模型类实例的列表
#[<Movie 1>, <Movie 2>]
Movie.query.count()  # 获取 Movie 模型所有记录的数量
#2
Movie.query.get(1)  # 获取主键值为 1 的记录
#<Movie 1>
Movie.query.filter_by(title='Mahjong').first()  # 获取 title 字段值为 Mahjong 的记录
#<Movie 2>
Movie.query.filter(Movie.title=='Mahjong').first()  # 等同于上面的查询，但使用不同的过滤方法
#<Movie 2>
