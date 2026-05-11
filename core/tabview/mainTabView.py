import customtkinter as tk

class MainTabview(tk.CTkTabview):
    def add_tab(self, name:str, frame:tk.CTkFrame) -> tk.CTkFrame:
        return self._c_insert(len(self._tab_dict), name, frame)
        
    def _c_insert(self, index: int, name: str, frame:tk.CTkFrame) -> tk.CTkFrame:
        if name not in self._tab_dict:
            # if no tab exists, set grid for segmented button
            if len(self._tab_dict) == 0:
                self._set_grid_segmented_button()

            self._name_list.append(name)
            self._tab_dict[name] = frame

            if self._fg_color == "transparent":
                self._tab_dict[name].configure(fg_color=self._apply_appearance_mode(self._bg_color),
                                                bg_color=self._apply_appearance_mode(self._bg_color))
            else:
                self._tab_dict[name].configure(fg_color=self._apply_appearance_mode(self._fg_color),
                                                bg_color=self._apply_appearance_mode(self._fg_color))

            self._segmented_button.insert(index, name)

            # if created tab is only tab select this tab
            if len(self._tab_dict) == 1:
                self._current_name = name
                self._segmented_button.set(self._current_name)
                self._grid_forget_all_tabs()
                self._set_grid_current_tab()

            return self._tab_dict[name]
        else:
            raise ValueError(f"CTkTabview already has tab named '{name}'")

    """ def add(self, name: str) -> CTkFrame:
        # appends new tab with given name
        return self.insert(len(self._tab_dict), name) """