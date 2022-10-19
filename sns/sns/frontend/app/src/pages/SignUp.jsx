import styled from "styled-components";
import { useNavigate } from "react-router-dom";

import { RichButton } from "../components/Elements/Button";
import { LoginForm } from "../components/Elements/LoginForm";

export const SignUp = () => {
    const navigate = useNavigate();

    const ContactTitle = styled.div`
        text-align: center;
    `;

    const createUser = () => {
        postToBackend("http://localhost:80/api/v1/users", {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
        }).then((data) => {
            if (data) {
                navigate("/");
            } else {
                alert("not 201");
            }
        });
    };

    const postToBackend = async (url = "", data = {}) => {
        const response = await fetch(url, {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
            },
            redirect: "follow",
            referrerPolicy: "no-referrer",
            body: JSON.stringify(data),
        });
        if (response.status === 201) {
            return response.json();
        } else {
            return null;
        }
    };

    return (
        <div>
            <form name="login_form">
                <ContactTitle>
                    <h1 className="contact-title">ユーザ作成</h1>
                </ContactTitle>
                <div>
                    <center>
                        <LoginForm />
                        <RichButton type="Sign Up" onClick={createUser} />
                    </center>
                </div>
            </form>
        </div>
    );
};
