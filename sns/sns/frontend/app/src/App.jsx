import { BrowserRouter, Link, Routes, Route } from "react-router-dom";

import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { SignUp } from "./pages/SignUp";

export const App = () => {
    return (
        <BrowserRouter>
            <div className="App">
                <Link to="/">Home</Link>
                <Link to="/login">Login</Link>
                <Link to="/signup">SignUp</Link>

                <Routes>
                    <Route exact path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/signup" element={<SignUp />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
};
