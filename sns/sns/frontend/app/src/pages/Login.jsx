import { useNavigate } from "react-router-dom";

import { RichButton } from "../components/Elements/Button";
import { LoginForm } from "../components/Elements/LoginForm";

import { createSession } from "/app/src/features/auth/api/createSession";

export const Login = () => {
    const navigate = useNavigate();
    const loginAccount = () => {
        createSession(
            document.getElementById("email").value,
            document.getElementById("password").value
        ).then(
            (result) => navigate("/users"),
            (error) => navigate("/forbidden")
        );
    };

    return (
        <div>
            <form name="login_form">
                <center>
                    <h1 className="contact-title">ログイン</h1>
                </center>
                <div>
                    <center>
                        <LoginForm />
                        <RichButton type="login" onClick={loginAccount} />
                    </center>
                </div>
            </form>
        </div>
    );
};
