import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import styled from "styled-components";

import ChatRoundedIcon from "@mui/icons-material/ChatRounded";
import IconButton from "@mui/material/IconButton";

import { HeaderOnLogin } from "../components/layouts/Header";

export const UserHome = () => {
    const navigate = useNavigate();

    const PushButton = styled.div`
        position: absolute;
        right: 0;
        bottom: 0;
        padding: 15px;
    `;

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
    const user = {
        name: "unknown",
        icon: undefined,
    };
    return (
        <>
            <HeaderOnLogin user />
            <div>
                <ul id="userinfo"></ul>
            </div>
            <PushButton>
                <IconButton
                    size="large"
                    aria-label="account of current user"
                    aria-controls="menu-appbar"
                    aria-haspopup="true"
                    // onClick={handleMenu}
                    color="inherit"
                >
                    <ChatRoundedIcon fontSize="large" color="primary" />
                </IconButton>
            </PushButton>
        </>
    );
};
