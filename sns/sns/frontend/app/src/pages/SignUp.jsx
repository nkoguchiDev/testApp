import styled from "styled-components";

export const SignUp = () => {
    const ContactTitle = styled.div`
        text-align: center;
    `;

    const createUser = () => {
        postToBackend("http://localhost:80/api/v1/users", {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
        }).then((data) => {
            if (data) {
                window.location.href = "/";
            } else {
                console.log("not 201");
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
                <ContactTitle>
                    <p>
                        Email, Passwordご入力の上, 「作成」ボタンをクリックしてください.
                    </p>
                </ContactTitle>
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
                            <button type="button" onClick={createUser}>
                                作成
                            </button>
                        </div>
                    </center>
                </div>
            </form>
        </div>
    );
};
