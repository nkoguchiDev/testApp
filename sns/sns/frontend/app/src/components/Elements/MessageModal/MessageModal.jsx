import * as React from "react";
import IconButton from "@mui/material/IconButton";
import ChatRoundedIcon from "@mui/icons-material/ChatRounded";

import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";

import { createMessage } from "../../../features/messages/api/createMessage";

export const MessageModal = () => {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const pushOK = () => {
        const content = document.getElementById("body").value;
        createMessage(content);
        setOpen(false);
    };
    const pushCancel = () => {
        setOpen(false);
    };

    return (
        <div>
            <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                color="inherit"
                onClick={handleOpen}
            >
                <ChatRoundedIcon fontSize="large" color="primary" />
            </IconButton>
            <Dialog open={open} onClose={pushCancel}>
                <DialogTitle>Message</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        ポストするメッセージを入力してください
                    </DialogContentText>
                    <TextField
                        autoFocus
                        id="body"
                        margin="dense"
                        label="本文"
                        variant="standard"
                        multiline
                        fullWidth
                        minRows={10}
                        maxRows={20}
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={pushCancel}>Cancel</Button>
                    <Button onClick={pushOK}>OK</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
};
