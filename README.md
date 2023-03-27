# PremierLeague
プレミアリーグの順位表をWebページからスクレイピングし、PythonのTkinterライブラリを使ってグラフィカルな表形式で表示するプログラムです。具体的には、順位、チーム名、ポイント数のデータを取得し、Tkinterを使用してウィンドウ上に表示します。

## 手順：
プレミアリーグの順位表をWebページ（https://www.transfermarkt.com/premier-league/tabelle/wettbewerb/GB1）からスクレイピングし、リスト形式で返します。このリストは、順位、チーム名、ポイント数のデータを含みます。


create_table 関数は、Tkinterの ttk.Treeview ウィジェットを使用して、グラフィカルな表形式で順位表データを表示します。この表には、順位、チーム名、ポイント数が表示されます。


main 関数は、上記の2つの関数を呼び出して、順位表データを取得し、Tkinterのウィンドウに表示します。このウィンドウには、プレミアリーグの順位表が表示されます。


プログラムが直接実行されている場合（__name__ == '__main__'）、main 関数が呼び出されます。これにより、ウィンドウが表示され、プレミアリーグの順位表が表示されます。
