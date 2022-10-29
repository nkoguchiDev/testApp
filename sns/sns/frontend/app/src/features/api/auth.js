import { axios } from "/app/src/lib/axios";

export const createSession = (email, password) => {
    return axios.post(
        "/session",
        { email, password },
        {
            headers: {
                "Content-Type": "application/json",
            },
            withCredentials: true,
        }
    );
};
