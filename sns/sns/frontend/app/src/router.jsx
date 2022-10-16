import { Route, Routes, Navigate } from "react-router-dom";

import { Home } from "./pages/Home";
import { UserHome } from "./pages/UserHome";
import { Login } from "./pages/Login";
import { SignUp } from "./pages/SignUp";
import { Forbidden } from "./pages/Forbidden";

export const AppRouter = () => {
    return (
        <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/users" element={<UserHome />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/forbidden" element={<Forbidden />} />
        </Routes>
    );
};
