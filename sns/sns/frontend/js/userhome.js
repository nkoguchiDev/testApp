function getUserInformation() {
    getData("http://127.0.0.1:80/api/v1/me").then((data) => {
        if (data === false) {
            location = "no_permission.html";
        }

        const element = document.getElementById("userinfo");

        const li_email = document.createElement("li");
        li_email.textContent = "email: " + data.email;
        element.appendChild(li_email);

        // 最後の子要素として追加
        const li_is_active = document.createElement("li");
        li_is_active.textContent = "is_active: " + data.is_active;
        element.appendChild(li_is_active);
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
