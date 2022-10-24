import { axios } from "/app/src/lib/axios";

export const createMessage = (content) => {
    return axios.post(
        "/messages",
        { content },
        {
            headers: {
                "Content-Type": "application/json",
            },
        }
    );
};
