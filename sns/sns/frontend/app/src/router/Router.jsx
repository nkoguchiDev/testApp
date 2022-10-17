import { Route, Routes } from "react-router-dom";

import { Home } from "../pages/Home";
import { UserHome } from "../pages/UserHome";
import { Login } from "../pages/Login";
import { SignUp } from "../pages/SignUp";
import { Forbidden } from "../pages/Forbidden";

import { Header } from "../components/layouts/Header/Header";

export const Router = () => {
    return (
        <Routes>
            <Route
                exact
                path="/"
                element={
                    <>
                        <Header />
                        <Home />
                    </>
                }
            />
            <Route
                path="/users"
                element={
                    <>
                        <Header />
                        <UserHome />
                    </>
                }
            />
            <Route
                path="/login"
                element={
                    <>
                        <Header />
                        <Login />
                    </>
                }
            />
            <Route
                path="/signup"
                element={
                    <>
                        <Header />
                        <SignUp />
                    </>
                }
            />
            <Route
                path="/forbidden"
                element={
                    <>
                        <Header />
                        <Forbidden />
                    </>
                }
            />
        </Routes>
    );
};
