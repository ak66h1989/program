using SQLite
using DataArrays, DataFrames
using DataFramesMeta
pwd()
cd("C:\\Users\\ak66h_000\\Documents\\db\\")
db = SQLite.DB("tse.sqlite3")
close=SQLite.query(db, "SELECT * FROM close")
print(close)
value=SQLite.query(db, "SELECT * FROM value")
print(value)

db = SQLite.DB("mops.sqlite3")
df=SQLite.query(db, "SELECT * FROM `ifrs前後-資產負債表-一般業`")
df=SQLite.query(db, "SELECT name FROM sqlite_master WHERE type='table';")
close[1,:最後揭示買量]
isnull(close[1,:最後揭示買量])
[NA for x in close[:最後揭示買量] if isnull(x)]

close[isnull(close[:最後揭示買量])]
close[isna(close[:最後揭示買量]),:最後揭示買量] = NA
value[3,:本益比].value=="-"
df=@where(value, :本益比.=="-")
df=value[value[:本益比].=="16.29",:]
df=DataFrame(a=1:10,本益比=1:10)
value[1,:本益比]
Float64(value[1,:本益比])
df1=df[df[:本益比].==1,:]
df1=value[isnull(value[:本益比]),:]
print(df1)
filter(x -> isnull(x), close[:最後揭示買量])
col[1]
push!(col,:abc)
[1,"a"]
using DataFrames, RDatasets
[x for x in iris[:PetalWidth]]
iris = dataset("datasets", "iris")
print(iris)
df=iris[iris[:Species].=="setosa",:]
print(df)

df=by(iris, [:Species, :PetalWidth], size)
df=by(iris, :Species, size)
df=by(iris, :Species, df -> mean(df[:PetalLength]))
df=by(iris, :Species, df -> DataFrame(N = size(df, 1)))
df=by(iris, :Species) do df
    DataFrame(m = mean(df[:PetalLength]), s² = var(df[:PetalLength]))
end
df=by(iris, :Species, df -> df[1:end-1,:PetalLength])
df=by(iris, :Species, df -> df)
df=aggregate(iris, :Species, sum)
df=aggregate(iris, :Species, [sum, mean])
for subdf in groupby(iris, :Species)
    println(size(subdf, 1))
end
print(iris.colindex.names)
print(df)
df[2:end,:PetalLength]=df[1:end-1,:PetalLength]
df[1,:PetalLength]=NA
col=[:SepalLength,:SepalWidth,:PetalLength,:PetalWidth]
col=iris.colindex.names[1:end-1]
iris1=deepcopy(iris)

function lag(df, i, col)
  df[1+i:end,col]=df[1:end-i,col]
  df[1:i,col]=NA
  return df[col]
end
print(lag(iris, 1))
df=by(iris1, :Species, df->lag(df,1, col))
df=by(iris, :Species, df -> df[2:end,col]=df[1:end-1,col] df[1,col]=NA)
names(df)[5]=:本益比
showcols(df)
iris[:id] = 1:size(iris, 1)  # this makes it easier to unstack
d = stack(iris, [1:4])
d = stack(iris, [:SepalLength, :SepalWidth, :PetalLength, :PetalWidth])
d = stack(iris, [:SepalLength, :SepalWidth], :Species)
d = melt(iris, :Species)
d = stackdf(iris)
print(d)
longdf = melt(iris, :id)
print(longdf)
widedf = unstack(longdf, :id, :variable, :value)
size(iris)
sort!(iris)
sort!(iris, cols = [order(:Species, by = lowercase),
                    order(:SepalLength, rev = false)])
Float64(iris[:SepalLength])
print(df[1:end,:SepalLength])
df.head()
df[1,:本益比]
replace("string", "t", "a")

join(df, value, on = [:年月日, :證券代號, :證券名稱, :本益比], kind = :outer)
print(df[end])
