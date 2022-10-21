import { axios } from "/app/src/lib/axios";

export const createUser = (email, password) => {
    return axios.post(
        "/users",
        { email, password },
        {
            headers: {
                "Content-Type": "application/json",
            },
        }
    );
};
