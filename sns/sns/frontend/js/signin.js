function nextPage() {
    em = document.getElementById("email").value;
    pwd = document.getElementById("password").value;

    postData("http://127.0.0.1:80/api/v1/session", {
        email: em,
        password: pwd,
    }).then((data) => {
        if (data) {
            location = "userhome.html";
        } else {
            location = "no_permission.html";
        }
    });
}

// POST メソッドの実装の例
async function postData(url = "", data = {}) {
    // 既定のオプションには * が付いています
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "include", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data),
    });
    if (response.status === 201) {
        return true;
    }
    return false;
}
