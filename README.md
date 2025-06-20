# python の 1000 本ノック

## 目的

python の記法や pythonic な書き方が体に定着していないので、息を吐くように記述できるように練習するため。

## 問題

ChatGPT に出力させる。
お作法や型定義等の堅牢性も含めて、ランダムな分野（配列処理や重めなロジックなど）で出題するように指示。

## どこまでやる？

例えば、配列処理を行う際に JS では高階関数（`numbers.filter(x => x % 2 === 0).map(x => x * x)`）の使用が好まれている。
対して、Python ではリスト内包表記（`squares = [x * x for x in numbers if x % 2 == 0]`）がよく利用されている。
こういったことから、pythonic な書き方が体に馴染むまで行う。

## 実行方法

単純に.pyファイルを実行する場合
```
poetry run python3 src/xxx.py 
```

テスト実行
```
poetry run test
```