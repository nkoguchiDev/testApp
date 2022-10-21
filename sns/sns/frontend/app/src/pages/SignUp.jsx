import styled from "styled-components";
import { useNavigate } from "react-router-dom";

import { RichButton } from "../components/Elements/Button";
import { LoginForm } from "../components/Elements/LoginForm";

import { createUser } from "/app/src/features/users/api/createUser";

export const SignUp = () => {
    const navigate = useNavigate();

    const ContactTitle = styled.div`
        text-align: center;
    `;

    const createAccount = () => {
        createUser(
            document.getElementById("email").value,
            document.getElementById("password").value
        ).then(
            (result) => navigate("/"),
            (error) => alert("please retry")
        );
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
                        <RichButton type="Sign Up" onClick={createAccount} />
                    </center>
                </div>
            </form>
        </div>
    );
};
