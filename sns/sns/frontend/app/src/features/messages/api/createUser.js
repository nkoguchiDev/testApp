import { axios } from "/app/src/lib/axios";

export const createUser = (email, password, display_name) => {
    return axios.post(
        "/users",
        { email, password, display_name },
        {
            headers: {
                "Content-Type": "application/json",
            },
        }
    );
};
