// axios使う
axios.defaults.baseURL = "http://localhost:80";

function file_upload_reservation() {
    return new Promise((resolve, reject) => {
        axios({
            method: "post",
            url: "/images",
        })
            .then(function (response) {
                // 成功時に実行
                // response.dataに実際のデータが入っている
                let result = response.data;
                resolve(result);
            })
            .catch(function (error) {
                // エラー時に実行
                reject(error);
            })
            .then(function () {
                // 常に実行
            });
    });
}

let file = null;

document.getElementById("fileUpload").onchange = function ({ target: { files } }) {
    file = files[0];
};
// upload
document.getElementById("uploadBtn").onclick = async function () {
    if (!file) return;
    // スライスプール作成
    let size = 1024 * 1024 * 0.1; // スライスサイズ設定 2MB
    let fileChunks = [];
    let index = 0; // index値
    for (let cur = 0; cur < file.size; cur += size) {
        fileChunks.push({
            hash: index++,
            chunk: file.slice(cur, cur + size),
        });
    }

    const data = await file_upload_reservation();

    const uploadFileChunks = async function (upload_id, list) {
        if (list.length === 0) {
            await axios({
                method: "post",
                url: "/images" + "/" + upload_id + "/merge",
            });
            return;
        }
        // 非同期並行処理
        let pool = []; // 並行処理プール
        let max = 3; // 最大並行処理数
        let finish = 0; // 送信完了数
        let failList = []; // 失敗リスト
        for (let i = 0; i < fileChunks.length; i++) {
            let item = fileChunks[i];
            let formData = new FormData();
            formData.append("filename", file.name);
            formData.append("hash", item.hash);
            formData.append("chunk", item.chunk);
            // アップロードタスク
            let task = axios({
                method: "post",
                url: "/images" + "/" + data.id,
                data: formData,
            })
                .then((data) => {
                    let index = pool.findIndex((t) => t === task);
                    pool.splice(index);
                })
                .catch(() => {
                    failList.push(item);
                })
                .finally(() => {
                    finish++;
                    // すべてアップロード完了後処理
                    if (finish === fileChunks.length) {
                        uploadFileChunks(data.id, failList);
                    }
                    console.log(finish, fileChunks.length);
                });

            pool.push(task);
            if (pool.length === max) {
                // 並行処理最大数超えないように制御
                await Promise.race(pool);
            }
        }
    };

    uploadFileChunks(data.id, fileChunks);
};
