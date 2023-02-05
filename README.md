本リポジトリの導入
=======================

Chrome, Pythonおよびpipのインストール(Windows版)
------------------
以下のリンクの手順を参考にchrome, pythonとpipをインストール.

Chromeは[こちら](https://cs.zaq.ne.jp/knowledgeDetail?an=001440866&did=faq_alert_link)を参照.

注意: **python3.8** をインストールしてください.

PythonとPipのインストールは[こちら](https://wepicks.net/weplog-pip_win10/)を参照.


リポジトリのクローン
-----------------

以下のコマンドを1行ずつ入力.
```
git clone -b master https://github.com/nakaotatsuya/address_collector.git
cd address_collector
pip install -r requirements.txt
```

Usage
------

1. Download Data

`pref_id` に都道府県ID(1-47)を,`city_id` に市町村ID(1-xxx)を入力する.市町村IDの数は、各都道府県により異なる.
以下は例. `pref_id`が11(奈良県),`city_id`が1(五條市)の全ての住所のcsvファイルをダウンロードする.

(Recommended)
```
python test_selenium.py --pref_id 11 --city_id 1 --year 2020 --userID "<userID>" --password "<password>"
```

`city_id` に何も入力しなければ,`pred_id` で指定した都道府県の全市町村に関してダウンロードを行う(が,非常に時間がかかるため推奨されない.)
以下のコマンドでは,奈良県の全ての市町村の住所のcsvファイルをダウンロードする.
(Not Recommended)
```
python test_selenium.py --pref_id 11 --year 2020 --userID "<userID>" --password "<password>"
```

`year` は現在のところ2020年など最新が見れないため,2012年をデフォルトとしている.


2. Combine Data

ダウンロードしてきたデータに対し,データの結合を行う.
以下の例では,`pref_id`が11(奈良県),`city_id`が1(五條市)のすべての住所に関して結合を行う.

```
python combine.py --pref_id 11 --city_id 1
```

また、`city_id`を指定しなければ, `pref_id`で指定した都道府県の各市町村に関して住所の結合を行う. (都道府県以下ですべて結合するという意味ではなく,あくまで結合は市町村以下の住所で行われる.例えば, 〇〇県xx市,〇〇県yy市,〇〇県zz市があれば,xx市内のすべての住所で結合したcsvファイルが1つ,yy市内のすべての住所で結合したcsvファイルが1つ,zz市内のすべての住所で結合したcsvファイルが1つなどという具合.)

```
python combine.py --pref_id 11
```

`/data/11/1/combined_data/`以下に結合されたcsvファイルが生成されているか確認する.



