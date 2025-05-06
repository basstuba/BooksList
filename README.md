# Django × docker × mysql の雛形

## 使用方法

1. 任意のディレクトリにクローン作成
    ```
    git clone git@github.com:basstuba/Django_sample.git
    ```
2. リポジトリ名変更
    ```
    mv Django_sample 新しいリポジトリ名
    ```
3. .env作成
    ```
    cp .env.example .env
    ```
4. コンテナ作成
    ```
    make up
    ```
5. シークレットキー作成
    ```
    make secretkey
    ```
6. 作成したシークレットキーを.envのSECRET_KEYの値にコピペ

## ローカル環境に仮想環境を作成（VS Code の補完・警告解消の用のため任意）

1. 下記のコマンドで作成
    ```
    make venv
    ```
2. VS Codeを再起動して、VS Code下部のPythonバージョンを **.venv** のものに設定

## 各種コマンド

- Makefile参照

## その他
- アプリの追加はsrc/appsにする
- アプリ追加後、settings.pyのINSTALLED_APPSに'apps.core',のように追記
- アプリ追加後、アプリ/apps.pyのnameも'apps.core'のようにsettings.pyのINSTALLED_APPSと揃える
