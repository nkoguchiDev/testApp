import { BrowserRouter, Link, Routes, Route } from "react-router-dom";
import styled from "styled-components";

import { Home } from "../../../pages/Home";
import { Login } from "../../../pages/Login";
import { SignUp } from "../../../pages/SignUp";

import "./style.css";

export const Header = () => {
    // style
    const HeaderBar = styled.ul`
        text-align: center;
        padding: 10px 0;
        margin: 0 auto;
    `;
    const HeaderBarItem = styled.li`
        list-style: none;
        display: inline-block;
        margin: 0 20px;
    `;
    // contents
    return (
        <BrowserRouter>
            <div>
                <HeaderBar>
                    <HeaderBarItem>
                        <Link to="/">Home</Link>
                    </HeaderBarItem>
                    <HeaderBarItem>
                        <Link to="/login">Login</Link>
                    </HeaderBarItem>
                    <HeaderBarItem>
                        <Link to="/signup">SignUp</Link>
                    </HeaderBarItem>
                </HeaderBar>

                <Routes>
                    <Route exact path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/signup" element={<SignUp />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
};
