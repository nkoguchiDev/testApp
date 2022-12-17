"""
バイナリファイルを分割/結合するスクリプト

License: MIT
Created at: 2021/03/11
"""
import os
import sys


def split_bin_file(srcfname, chunk, outdir):
    """
    srcfnameのバイナリファイルをchunkのサイズで分割し、outdir以下に分割したファイルを作成する
    """
    with open(srcfname, 'rb') as fin:  # バイナリファイルとして開く
        split_bin_stream(fin, srcfname, chunk, outdir)  # 処理を委譲


def split_bin_stream(fin, srcfname, chunk, outdir):
    """
    finのストリームをchunkのサイズで分割し、outdir以下にsrcfnameの連番で分割したファイルを作成する
    """
    if not os.path.exists(outdir):  # ディレクトリが存在しないなら
        os.mkdir(outdir)  # 作成

    i = 0  # 連番
    while True:
        data = fin.read(chunk)  # chunkサイズだけ読み込む
        if not len(data):  # 読み込みが空ならループから抜ける
            break

        outfname = f'{srcfname}.{i}'  # ファイル名を合成
        outpath = os.path.join(outdir, outfname)  # パスを作成
        write_data(outpath, data)  # データを書き込む

        i += 1  # 連番のインクリメント


def write_data(path, data):
    """
    pathをバイナリファイルとして開きdataを書き込む
    """
    with open(path, 'wb') as fout:
        fout.write(data)


def join_bin_files(dstfname, files):
    """
    dstfnameのバイナリファイルににfilesのファイル群を結合して保存する
    """
    with open(dstfname, 'wb') as fout:
        for file in files:
            with open(file, 'rb') as fin:
                fout.write(fin.read())


def main():
    """
    コマンドで分割/結合を分岐する（テスト用）

    使用例:
        python split.py split
        python split.py join
    """
    if len(sys.argv) < 2:
        print('python split.py [split|join]')
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == 'split':
        split_bin_file('file.dat', 4, 'app/out')
    elif cmd == 'join':
        join_bin_files('join.dat', [
            'app/out/file.dat.0',
            'app/out/file.dat.1',
            'app/out/file.dat.2',
        ])


if __name__ == '__main__':
    main()
