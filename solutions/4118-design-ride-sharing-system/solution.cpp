class RideSharingSystem {
public:
deque<int> riders;
deque<int> drivers;

RideSharingSystem() {}

void addRider(int riderId) {
riders.push_back(riderId);
}

void addDriver(int driverId) {
drivers.push_back(driverId);
}

vector<int> matchDriverWithRider() {
if (!riders.empty() && !drivers.empty()) {
int d = drivers.front();
int r = riders.front();
drivers.pop_front();
riders.pop_front();
return {d, r};
}
return {-1, -1};
}

void cancelRider(int riderId) {
for (int i = 0; i < (int)riders.size(); ++i) {
if (riders[i] == riderId) {
riders.erase(riders.begin() + i);
break;
}
}
}
};
