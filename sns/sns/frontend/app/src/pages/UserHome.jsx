import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import styled from "styled-components";

import ChatRoundedIcon from "@mui/icons-material/ChatRounded";
import IconButton from "@mui/material/IconButton";

import { HeaderOnLogin } from "../components/layouts/Header";
import { getUserProfile } from "/app/src/features/users/api/getUserProfile";
import { EventCard } from "../components/Elements/EventCard";

const PushButton = styled.div`
    position: absolute;
    right: 0;
    bottom: 0;
    padding: 15px;
`;

export const UserHome = () => {
    const navigate = useNavigate();

    useEffect(() => {
        return () => {
            getUserInformation();
        };
    });

    const getUserInformation = () => {
        getUserProfile().then(
            (result) => {
                const element = document.getElementById("userinfo");

                const li_email = document.createElement("li");
                li_email.textContent = "email: " + result.email;
                element.appendChild(li_email);

                const li_display_name = document.createElement("li");
                li_display_name.textContent = "display name: " + result.display_name;
                element.appendChild(li_display_name);

                // 最後の子要素として追加
                const li_is_active = document.createElement("li");
                li_is_active.textContent = "is_active: " + result.is_active;
                element.appendChild(li_is_active);
            },
            (error) => navigate("/forbidden")
        );
    };

    return (
        <>
            <HeaderOnLogin user />
            <div>
                <ul id="userinfo"></ul>
            </div>
            <EventCard />
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
