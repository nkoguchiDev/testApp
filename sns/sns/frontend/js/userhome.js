function getUserInformation() {
    getData("http://localhost:80/api/v1/me").then((data) => {
        if (data === false) {
            alert("権限がありません");
        }
    });
}

// POST メソッドの実装の例
async function getData(url = "") {
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "include",
        redirect: "follow",
        referrerPolicy: "no-referrer",
    });
    if (response.status === 200) {
        return response.json();
    }
    return false;
}
