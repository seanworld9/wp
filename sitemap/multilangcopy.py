
dlla_list = ["de", "es", "fr", "hu",  "id", "it", "ko", "nl", "pl", "pt-pt", "ru", "tr", "zh"]

for x in dlla_list:
	
    # ファイルを読み込む
    with open('/home/seanworld9/wp/sitemap/sitemap_en.xml', 'r', encoding='UTF-8') as file:
        # ファイルの内容を読み込む
        content = file.read()

    # '/en/' を '/de/' に置換
    content = content.replace('/en/', '/'+ x +'/')

    # 置換した内容を新しいファイルに書き込む
    with open('/home/seanworld9/wp/docs/'+x +'/sitemap.xml', 'w', encoding='UTF-8') as file:
        file.write(content)

    print(x+'/sitemap.xml has been created.')


