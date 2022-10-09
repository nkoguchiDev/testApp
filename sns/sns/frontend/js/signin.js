function nextPage() {
    id = document.getElementById("email").value;
    pwd = document.getElementById("password").value;

    const data = {
        email: id,
        password: pwd,
    };

    const XHR = new XMLHttpRequest();

    // エラーが発生した場合に行うことを定義します
    XHR.addEventListener("error", function (event) {
        alert("Oops! Something went wrong.");
    });

    // リクエストをセットアップします
    XHR.open("POST", "http://localhost:80/api/v1/session");

    XHR.setRequestHeader("Content-Type", "application/json");
    // 最後に、データを送信します
    XHR.send(JSON.stringify(data));
}
