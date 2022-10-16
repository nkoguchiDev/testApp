import { BrowserRouter, Link, Routes, Route } from "react-router-dom";

import { UserHome } from "../pages/UserHome";
import { Forbidden } from "../pages/Forbidden";

export const Login = () => {
    function createSession() {
        postToBackend("http://localhost:80/api/v1/session", {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
        }).then((data) => {
            if (data) {
                return (
                    <Routes>
                        <Route path="/users" element={<UserHome />} />
                    </Routes>
                );
            } else {
                return (
                    <Routes>
                        <Route path="/forbidden" element={<Forbidden />} />
                    </Routes>
                );
            }
        });
    }

    async function postToBackend(url = "", data = {}) {
        const response = await fetch(url, {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            redirect: "follow",
            referrerPolicy: "no-referrer",
            body: JSON.stringify(data),
        });
        if (response.status === 201) {
            return true;
        }
        return false;
    }
    return (
        <div>
            <form name="login_form">
                <center>
                    <h1 className="contact-title">ログイン</h1>
                </center>
                <center>
                    <p>
                        Email, Passwordご入力の上,
                        「ログイン」ボタンをクリックしてください.
                    </p>
                </center>
                <div>
                    <center>
                        <div>
                            <input
                                type="email"
                                name="email"
                                id="email"
                                placeholder="Email"
                            />
                        </div>
                        <br />
                        <div>
                            <input
                                type="password"
                                name="pass"
                                id="password"
                                placeholder="Password"
                                onchange="validation();"
                            />
                        </div>
                        <div>
                            <button type="button" onClick={createSession}>
                                ログイン
                            </button>
                        </div>
                    </center>
                </div>
            </form>
        </div>
    );
};
