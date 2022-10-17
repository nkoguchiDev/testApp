import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export const UserHome = () => {
    const navigate = useNavigate();

    useEffect(() => {
        return () => {
            getUserInformation();
        };
    });

    function getUserInformation() {
        getData("http://localhost:80/api/v1/me").then((data) => {
            if (data === false) {
                navigate("/forbidden");
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
    return (
        <div>
            <ul id="userinfo"></ul>
        </div>
    );
};
