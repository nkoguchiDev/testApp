import { HeaderOnLogin } from "../components/layouts/Header";
import { EventCard } from "../components/Elements/EventCard";
import { MessageModal } from "../components/Elements/MessageModal";

export const UserHome = () => {
    return (
        <>
            <HeaderOnLogin user />
            <div>
                <ul id="userinfo"></ul>
            </div>
            <EventCard />
            <MessageModal />
        </>
    );
};
